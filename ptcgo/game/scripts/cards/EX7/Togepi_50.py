from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="71d555e2-e39d-5980-a667-49e2993a473f",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Togepi.Name",
    display_name="Togepi",
    searchable_by=["Togepi", "Basic", "Togepi"],
    subtypes=["Basic"],
    collector_number=50,
    set_code="EX7",
    rarity=Rarities.Uncommon,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=175,
    abilities=[
        Attack(
            title="Yawn",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Mini-Metronome",
            game_text="Flip a coin. If heads, choose 1 of the Defending Pok\u00e9mon's attacks. Mini-Metronome copies that attack except for its Energy cost. (You must still do anything else required for that attack.) (No matter what type that Pok\u00e9mon is, Togepi's type is still Colorless.) Togepi performs that attack.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
    ],
)