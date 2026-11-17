from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cf32a9c2-12d1-56f0-ba39-48b600279573",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaMalamarex.Name",
    display_name="Mega Malamar ex",
    searchable_by=["Mega Malamar ex", "Stage 1", "MEGA", "ex", "MegaMalamarex"],
    subtypes=["Stage 1", "MEGA", "ex"],
    collector_number=69,
    set_code="ME6",
    rarity=Rarities.Rare,
    hp=320,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Inkay.Name",
    family_id=686,
    abilities=[
        Attack(
            title="Psychic Marionette",
            game_text="This attack does 70 damage for each of your opponent's Benched Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=70,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Eerie Wave",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.DARKNESS: 3},
            damage=200,
            effect=unimplemented,
        ),
    ],
)