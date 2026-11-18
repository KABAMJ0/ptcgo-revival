from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1c0988e4-6df8-5396-9485-17ea98c34cf7",
    key="SV6PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Crobat.Name",
    display_name="Crobat",
    searchable_by=["Crobat", "Stage 2", "Crobat"],
    subtypes=["Stage 2"],
    collector_number=29,
    set_code="SV6PT5",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Golbat.Name",
    family_id=41,
    abilities=[
        Ability(
            title="Shadowy Envoy",
            game_text="Once during your turn, if you played Janine's Secret Art from your hand this turn, you may draw cards until you have 8 cards in your hand.",
            effect=unimplemented,
        ),
        Attack(
            title="Poison Fang",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned. During Pok\u00e9mon Checkup, put 2 damage counters on that Pok\u00e9mon instead of 1.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=unimplemented,
        ),
    ],
)