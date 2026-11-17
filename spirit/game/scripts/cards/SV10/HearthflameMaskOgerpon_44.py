from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cea2d7de-f836-5e2a-9f2e-e218b9903404",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HearthflameMaskOgerpon.Name",
    display_name="Hearthflame Mask Ogerpon",
    searchable_by=["Hearthflame Mask Ogerpon", "Basic", "HearthflameMaskOgerpon"],
    subtypes=["Basic"],
    collector_number=44,
    set_code="SV10",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=1017,
    abilities=[
        Attack(
            title="Fire Kagura",
            game_text="Search your deck for a Basic Fire Energy card and attach it to 1 of your Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Searing Flame",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=unimplemented,
        ),
    ],
)