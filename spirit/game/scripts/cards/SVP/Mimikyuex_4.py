from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f88dcd7c-de83-5ce0-b296-f2ea9da03329",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mimikyuex.Name",
    display_name="Mimikyu ex",
    searchable_by=["Mimikyu ex", "Basic", "ex", "Mimikyuex"],
    subtypes=["Basic", "ex"],
    collector_number=4,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=190,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=778,
    abilities=[
        Attack(
            title="Void Return",
            game_text="You may switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Energy Burst",
            game_text="This attack does 30 damage for each Energy attached to both Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)