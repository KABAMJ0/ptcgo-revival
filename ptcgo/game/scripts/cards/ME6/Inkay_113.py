from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.trainers import discard_from_opponent_hand

card = PokemonCardDef(
    guid="6ee2e711-453b-578e-8237-cadd9e5bff8b",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Inkay.Name",
    display_name="Inkay",
    searchable_by=["Inkay", "Basic", "Inkay"],
    subtypes=["Basic"],
    collector_number=113,
    set_code="ME6",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=686,
    abilities=[
        Attack(
            title="Knock Off",
            game_text="Discard a random card from your opponent's hand.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
            effect=discard_from_opponent_hand(),
        ),
    ],
)