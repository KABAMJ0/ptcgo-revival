from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5ee7ec24-7452-5c86-9a64-c1cea892eedb",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Heatran.Name",
    display_name="Heatran",
    searchable_by=["Heatran", "Basic", "Heatran"],
    subtypes=["Basic"],
    collector_number=88,
    set_code="SM5",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=485,
    abilities=[
        Attack(
            title="Guard Press",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Boiling Impact",
            game_text="Discard 2 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=unimplemented,
        ),
    ],
)