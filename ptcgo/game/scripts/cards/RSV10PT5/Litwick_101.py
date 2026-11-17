from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="184c5ef7-eb5f-5023-90c5-1f9d582f5351",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Litwick.Name",
    display_name="Litwick",
    searchable_by=["Litwick", "Basic", "Litwick"],
    subtypes=["Basic"],
    collector_number=101,
    set_code="RSV10PT5",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=607,
    abilities=[
        Attack(
            title="Brighten and Burn",
            game_text="Look at the top card of your deck. You may discard that card.",
            cost={PokemonTypes.FIRE: 1},
            effect=unimplemented,
        ),
    ],
)