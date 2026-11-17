from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="70a6455d-b127-5d82-9ce5-7086277ee4bb",
    key="ME55C",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Metagross.Name",
    display_name="Metagross",
    searchable_by=["Metagross", "Stage 2", "Metagross"],
    subtypes=["Stage 2"],
    collector_number=11,
    set_code="ME55C",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.LIGHTNING, PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Metang.Name",
    family_id=376,
    abilities=[
        Ability(
            title="Delta Control",
            game_text="Once during your turn (before your attack), you may look at the top 4 cards of your deck, choose 1 of them, and put it into your hand. Put the 3 other cards on the bottom of your deck in any order. This power can't be used if Metagross is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Crush and Burn",
            game_text="You may discard as many Energy cards as you like attached to your Pok\u00e9mon in play. If you do, this attack does 30 damage plus 20 more damage for each Energy card you discarded.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.METAL: 1},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)