from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7bab3d24-415f-55b6-8b86-01ab74979be9",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Duskull.Name",
    display_name="Duskull",
    searchable_by=["Duskull", "Basic", "Duskull"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="SM3",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=355,
    abilities=[
        Attack(
            title="Dark Guidance",
            game_text="Put a Basic Pok\u00e9mon from your discard pile onto your Bench.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Spooky Shot",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)