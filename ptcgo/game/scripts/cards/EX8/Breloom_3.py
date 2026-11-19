from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import conditions_if, self_has_energy_of_type
from ptcgo.game.card_effects.passives_common import boost_own_next_turn

card = PokemonCardDef(
    guid="71c5fa53-2196-59e9-a794-bcd8fe881b81",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Breloom.Name",
    display_name="Breloom",
    searchable_by=["Breloom", "Stage 1", "Breloom"],
    subtypes=["Stage 1"],
    collector_number=3,
    set_code="EX8",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shroomish.Name",
    family_id=285,
    abilities=[
        Attack(
            title="Leaf Poison",
            game_text="If Breloom has any Grass Energy attached to it, the Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=conditions_if(self_has_energy_of_type(PokemonTypes.GRASS),
                                 SpecialConditions.POISONED),
        ),
        Attack(
            title="Hustle Punch",
            game_text="During your next turn, Hustle Punch attack's base damage is 50 instead of 70.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            damage_operator="-",
            effect=boost_own_next_turn(50 - 70, attack_title="Hustle Punch"),
        ),
    ],
)