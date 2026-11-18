from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="93fc82b8-ad2f-5197-973a-dc4f77eba956",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Krookodileex.Name",
    display_name="Krookodile ex",
    searchable_by=["Krookodile ex", "Stage 2", "ex", "Krookodileex"],
    subtypes=["Stage 2", "ex"],
    collector_number=55,
    set_code="ME4",
    rarity=Rarities.Rare,
    hp=320,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Krokorok.Name",
    family_id=553,
    abilities=[
        Attack(
            title="Corner",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=unimplemented,
        ),
        Attack(
            title="Strong Bite",
            game_text="If this Pok\u00e9mon has a Pok\u00e9mon Tool attached, this attack does 140 more damage.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=140,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)