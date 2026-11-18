from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="3726ff8e-e434-5423-992e-5509f3ba8140",
    key="SV6PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Munkidori.Name",
    display_name="Munkidori",
    searchable_by=["Munkidori", "Basic", "Munkidori"],
    subtypes=["Basic"],
    collector_number=72,
    set_code="SV6PT5",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    abilities=[
        Ability(
            title="Adrena-Brain",
            game_text="Once during your turn, if this Pok\u00e9mon has any Darkness Energy attached, you may move up to 3 damage counters from 1 of your Pok\u00e9mon to 1 of your opponent's Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Mind Bend",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)