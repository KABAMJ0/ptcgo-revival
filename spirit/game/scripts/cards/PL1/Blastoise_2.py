from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="225428cc-28c4-55a1-a0de-6f01e568ba93",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blastoise.Name",
    display_name="Blastoise",
    searchable_by=["Blastoise", "Stage 2", "Blastoise"],
    subtypes=["Stage 2"],
    collector_number=2,
    set_code="PL1",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wartortle.Name",
    family_id=7,
    abilities=[
        Ability(
            title="Dig Well",
            game_text="Once during your turn (before your attack), you may look at the top 3 cards of your deck, choose as many Water Energy cards as you like, and attach them to your Pok\u00e9mon in any way you like. Discard the other cards. This power can't be used if Blastoise is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Aqua Press",
            game_text="Does 20 damage plus 10 more damage for each Energy attached to all Pok\u00e9mon (both yours and your opponent's).",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Double Launcher",
            game_text="Discard 2 Energy attached to Blastoise. Choose 2 of your opponent's Benched Pok\u00e9mon. This attack does 60 damage to each of them. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) Blastoise can't use Double Launcher during your next turn.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
    ],
)