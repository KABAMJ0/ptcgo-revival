from ptcgo.game.card_effects.attacks_common import flip_or_nothing
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="fd973ae3-477c-555a-96c5-136f8b353988",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Houndour.Name",
    display_name="Houndour",
    searchable_by=["Houndour", "Basic", "Houndour"],
    subtypes=["Basic"],
    collector_number=204,
    set_code="SV3",
    rarity=Rarities.Rare,
    hp=50,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=228,
    abilities=[
        Attack(
            title="Coordinated Pack",
            game_text="For each of your Benched Houndour, search your deck for a Basic Darkness Energy card and attach it to that Houndour. Then, shuffle your deck.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Focus Fangs",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=flip_or_nothing(),
        ),
    ],
)