from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import extra_energy_beyond_cost
from ptcgo.game.card_effects.passives_common import guts_survive_passive

async def acme_of_heroism(ctx):
    await ctx.deal_damage()
    if extra_energy_beyond_cost(ctx) < 1 or ctx.attacker is None:
        return
    ctx.add_passive_through_opponents_turn(
        ctx.attacker,
        guts_survive_passive(hp_floor=10, flip=False, title="Acme of Heroism"),
    )


card = PokemonCardDef(
    guid="1b844222-3e72-593d-9ebc-fe3f6ada441b",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MarshadowMachampGX.Name",
    display_name="Marshadow & Machamp-GX",
    searchable_by=["Marshadow & Machamp-GX", "Basic", "TAG TEAM", "GX", "MarshadowMachampGX"],
    subtypes=["Basic", "TAG TEAM", "GX"],
    collector_number=82,
    set_code="SM10",
    rarity=Rarities.RareHolo,
    hp=270,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=68,
    abilities=[
        Attack(
            title="Revenge",
            game_text="If any of your Pok\u00e9mon were Knocked Out by damage from an opponent's attack during their last turn, this attack does 90 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Hundred-Blows Impact",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
        ),
        Attack(
            title="Acme of Heroism-GX",
            game_text="If this Pok\u00e9mon has at least 1 extra Energy attached to it (in addition to this attack's cost), and if it would be Knocked Out by damage from an opponent's attack during their next turn, it is not Knocked Out, and its remaining HP becomes 10. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=acme_of_heroism,
        ),
    ],
)