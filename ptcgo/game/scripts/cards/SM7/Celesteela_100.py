from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="35fb26d0-078a-58fb-a770-9da564cc24ec",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Celesteela.Name",
    display_name="Celesteela",
    searchable_by=["Celesteela", "Basic", "Ultra Beast", "Celesteela"],
    subtypes=["Basic", "Ultra Beast"],
    collector_number=100,
    set_code="SM7",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=797,
    abilities=[
        Attack(
            title="Moon Raker",
            game_text="If the total of both players' remaining Prize cards is exactly 6, this attack can be used for Metal.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 4},
            damage=160,
            effect=unimplemented,
        ),
    ],
)