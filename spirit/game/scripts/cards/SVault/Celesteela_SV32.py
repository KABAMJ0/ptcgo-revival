from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ff462083-b3f3-5670-9c76-9dfd07da83cb",
    key="SVault",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Celesteela.Name",
    display_name="Celesteela",
    searchable_by=["Celesteela", "Basic", "Ultra Beast", "Celesteela"],
    subtypes=["Basic", "Ultra Beast"],
    collector_number=32,
    set_code="SVault",
    rarity=Rarities.Rare,
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