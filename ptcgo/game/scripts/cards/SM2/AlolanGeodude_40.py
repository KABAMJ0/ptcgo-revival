from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.session.passives import Passive, carrier_pokemon


class _NoRetreatCostShield(Passive):
    """During your next turn the shielded Pokemon has no Retreat Cost."""

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        holder = carrier_pokemon(carrier) or carrier
        return 0 if holder is pokemon else cost


async def _rock_polish(ctx):
    target = ctx.attacker if ctx.attacker is not None else ctx.source
    if target is not None:
        ctx.add_passive_through_own_next_turn(target, _NoRetreatCostShield())


card = PokemonCardDef(
    guid="e3dce8e1-3a60-5d48-a096-2faff6b24550",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanGeodude.Name",
    display_name="Alolan Geodude",
    searchable_by=["Alolan Geodude", "Basic", "AlolanGeodude"],
    subtypes=["Basic"],
    collector_number=40,
    set_code="SM2",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    family_id=74,
    abilities=[
        Attack(
            title="Rock Polish",
            game_text="During your next turn, this Pok\u00e9mon has no Retreat Cost.",
            cost={},
            effect=_rock_polish,
        ),
        Attack(
            title="Rollout",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)