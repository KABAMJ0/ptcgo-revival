from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.session.passives import Passive, carrier_pokemon


class VulnerableNextTurnPassive(Passive):
    """Takes 100 more damage from attacks during the opponent's next turn."""

    def modify_damage_taken(self, calc, carrier):
        if calc.is_attack and calc.is_opposing \
                and carrier_pokemon(carrier) is calc.target:
            calc.amount += 100


async def plunging_headbutt(ctx):
    """Printed damage, then this Pokemon is 100 easier to damage next turn."""
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(ctx.attacker,
                                           VulnerableNextTurnPassive())


card = PokemonCardDef(
    guid="bad124fc-0e25-57c6-8f8e-740fd3350d08",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mabosstiff.Name",
    display_name="Mabosstiff",
    searchable_by=["Mabosstiff", "Stage 1", "Mabosstiff"],
    subtypes=["Stage 1"],
    collector_number=58,
    set_code="ME5",
    rarity=Rarities.Common,
    hp=140,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Maschiff.Name",
    family_id=942,
    abilities=[
        Attack(
            title="Bite",
            cost={PokemonTypes.DARKNESS: 2},
            damage=60,
        ),
        Attack(
            title="Plunging Headbutt",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 100 more damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.DARKNESS: 3},
            damage=210,
            effect=plunging_headbutt,
        ),
    ],
)