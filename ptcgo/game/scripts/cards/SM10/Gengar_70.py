from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1c982c04-d12c-5920-9f5e-90683eaf2ed4",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gengar.Name",
    display_name="Gengar",
    searchable_by=["Gengar", "Stage 2", "Gengar"],
    subtypes=["Stage 2"],
    collector_number=70,
    set_code="SM10",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Haunter.Name",
    family_id=92,
    abilities=[
        Ability(
            title="Shadow Pain",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may put 6 damage counters on your opponent's Pok\u00e9mon-GX and Pok\u00e9mon-EX in any way you like.",
            effect=unimplemented,
        ),
        Attack(
            title="Twilight Poison",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep and Poisoned.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
            effect=condition_attack(SpecialConditions.ASLEEP, SpecialConditions.POISONED),
        ),
    ],
)