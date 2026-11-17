from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1a012667-d91d-5c63-bc0d-32d3569db9d8",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gardevoir.Name",
    display_name="Gardevoir",
    searchable_by=["Gardevoir", "Stage 2", "Gardevoir"],
    subtypes=["Stage 2"],
    collector_number=8,
    set_code="PL1",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kirlia.Name",
    family_id=280,
    abilities=[
        Ability(
            title="Psychic Connect",
            game_text="As often as you like during your turn (before your attack), you may move a Psychic Energy attached to 1 of your Benched Pok\u00e9mon to your Active Pok\u00e9mon. This power can't be used if Gardevoir is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Energy Burst",
            game_text="Does 20 damage plus 10 more damage for each Energy attached to Gardevoir and the Defending Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Psychic Protection",
            game_text="Gardevoir has no Weakness during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=unimplemented,
        ),
    ],
)