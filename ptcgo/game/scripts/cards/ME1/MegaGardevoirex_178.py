from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="93a0685d-0da7-5b62-8422-bc0ae7de07b0",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaGardevoirex.Name",
    display_name="Mega Gardevoir ex",
    searchable_by=["Mega Gardevoir ex", "Stage 2", "MEGA", "ex", "MegaGardevoirex"],
    subtypes=["Stage 2", "MEGA", "ex"],
    collector_number=178,
    set_code="ME1",
    rarity=Rarities.Rare,
    hp=360,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kirlia.Name",
    family_id=280,
    abilities=[
        Attack(
            title="Overflowing Wishes",
            game_text="For each of your Benched Pok\u00e9mon, search your deck for a Basic Psychic Energy card and attach it to that Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Mega Symphonia",
            game_text="This attack does 50 damage for each Psychic Energy attached to all of your Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=50,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)