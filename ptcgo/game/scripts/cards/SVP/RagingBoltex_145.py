from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.trainers import discard_hand_draw

card = PokemonCardDef(
    guid="7cf78576-a1d1-51ac-8550-225baf81c5ba",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RagingBoltex.Name",
    display_name="Raging Bolt ex",
    searchable_by=["Raging Bolt ex", "Basic", "ex", "Ancient", "RagingBoltex"],
    subtypes=["Basic", "ex", "Ancient"],
    collector_number=145,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=240,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    abilities=[
        Attack(
            title="Burst Roar",
            game_text="Discard your hand and draw 6 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=discard_hand_draw(6),
        ),
        Attack(
            title="Bellowing Thunder",
            game_text="You may discard any amount of Basic Energy from your Pok\u00e9mon. This attack does 70 damage for each card you discarded in this way.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.FIGHTING: 1},
            damage=70,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)