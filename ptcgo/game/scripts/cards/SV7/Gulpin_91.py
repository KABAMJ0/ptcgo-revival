from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="8c9d5b4c-5ea7-5635-bfdb-ceaff110ee11",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gulpin.Name",
    display_name="Gulpin",
    searchable_by=["Gulpin", "Basic", "Gulpin"],
    subtypes=["Basic"],
    collector_number=91,
    set_code="SV7",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=316,
    abilities=[
        Attack(
            title="Drool",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
        ),
        Attack(
            title="Super Poison Breath",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.POISONED),
        ),
    ],
)