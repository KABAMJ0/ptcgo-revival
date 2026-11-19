from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="26b359f1-96bb-5504-990e-4c0bf59960da",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gligar.Name",
    display_name="Gligar",
    searchable_by=["Gligar", "Basic", "Gligar"],
    subtypes=["Basic"],
    collector_number=57,
    set_code="EX10",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=207,
    abilities=[
        Ability(
            title="Free Flight",
            game_text="If Gligar has no Energy cards attached to it, Gligar's Retreat Cost is 0.",
            effect=unimplemented,
        ),
        Attack(
            title="Toxic Grip",
            game_text="The Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.POISONED),
        ),
    ],
)