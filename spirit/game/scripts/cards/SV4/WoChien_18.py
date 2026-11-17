from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8fbf2233-198d-5734-8533-dd8b7c2c1643",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WoChien.Name",
    display_name="Wo-Chien",
    searchable_by=["Wo-Chien", "Basic", "WoChien"],
    subtypes=["Basic"],
    collector_number=18,
    set_code="SV4",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    family_id=1001,
    abilities=[
        Attack(
            title="Leaf Bringer",
            game_text="Attach up to 2 Basic Grass Energy cards from your discard pile to 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Binding Greed",
            game_text="During your opponent's next turn, attacks used by the Defending Pok\u00e9mon cost ColorlessColorless more.",
            cost={PokemonTypes.GRASS: 3, PokemonTypes.COLORLESS: 1},
            damage=140,
            effect=unimplemented,
        ),
    ],
)