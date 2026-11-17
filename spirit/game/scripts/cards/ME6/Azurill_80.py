from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="accf5c36-26e8-595e-b2ba-0caee0f8ef55",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Azurill.Name",
    display_name="Azurill",
    searchable_by=["Azurill", "Basic", "Azurill"],
    subtypes=["Basic"],
    collector_number=80,
    set_code="ME6",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=298,
    abilities=[
        Attack(
            title="Bouncy-Bounce Charge",
            game_text="Search your deck for an Energy card and attach it to 1 of your Benched Pok\u00e9mon. Then, shuffle your deck.",
            cost={},
            effect=unimplemented,
        ),
    ],
)