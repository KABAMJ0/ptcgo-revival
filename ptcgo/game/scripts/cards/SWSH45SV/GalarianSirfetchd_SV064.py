from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.session.legal_actions import LOCK_UNTIL_LEAVES_ACTIVE

async def meteor_assault(ctx):
    """180. Can't use Meteor Assault again until this Pokemon leaves Active."""
    await ctx.deal_damage()
    ctx.session.turn_state.attack_locks[
        (ctx.attacker.entity_id, ctx.ability.ability_id)
    ] = LOCK_UNTIL_LEAVES_ACTIVE

card = PokemonCardDef(
    guid="644356aa-2c7b-55a1-9123-47c999d89c4c",
    key="SWSH45SV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianSirfetchd.Name",
    display_name="Galarian Sirfetch'd",
    searchable_by=["Galarian Sirfetch'd", "Stage 1", "GalarianSirfetchd"],
    subtypes=["Stage 1"],
    collector_number=64,
    set_code="SWSH45SV",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianFarfetchd.Name",
    family_id=83,
    abilities=[
        Attack(
            title="Pierce",
            cost={PokemonTypes.FIGHTING: 1},
            damage=40,
        ),
        Attack(
            title="Meteor Assault",
            game_text="This Pok\u00e9mon can't use Meteor Assault again until it leaves the Active Spot.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=180,
            effect=meteor_assault,
        ),
    ],
)