from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="be684309-0915-5c57-bb1b-0b122d51c05d",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lombre.Name",
    display_name="Lombre",
    searchable_by=["Lombre", "Stage 1", "Lombre"],
    subtypes=["Stage 1"],
    collector_number=33,
    set_code="EX8",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lotad.Name",
    family_id=270,
    abilities=[
        Ability(
            title="Aqua Lift",
            game_text="If Lombre has any Water Energy attached to it, the Retreat Cost for Lombre is 0.",
            effect=unimplemented,
        ),
        Attack(
            title="Ambush",
            game_text="Flip a coin. If heads, this attack does 20 damage plus 20 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)