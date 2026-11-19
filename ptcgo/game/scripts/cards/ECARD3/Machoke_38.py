from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.passives_common import apply_own_next_turn_boost
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def _focus_energy(ctx):
    await ctx.deal_damage()
    await apply_own_next_turn_boost(ctx, 40, "Mega Punch")

card = PokemonCardDef(
    guid="745c4bec-a21f-555a-abe9-75ae0d94f93e",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Machoke.Name",
    display_name="Machoke",
    searchable_by=["Machoke", "Stage 1", "Machoke"],
    subtypes=["Stage 1"],
    collector_number=38,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Machop.Name",
    family_id=66,
    abilities=[
        Attack(
            title="Focus Energy",
            game_text="During your next turn, Machoke's Mega Punch attack's base damage is 80.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_focus_energy,
        ),
        Attack(
            title="Mega Punch",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)
