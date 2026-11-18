from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="641e2682-1567-5f05-a220-bedf7d76fc0e",
    key="HGSS3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gliscor.Name",
    display_name="Gliscor",
    searchable_by=["Gliscor", "Stage 1", "Gliscor"],
    subtypes=["Stage 1"],
    collector_number=4,
    set_code="HGSS3",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gligar.Name",
    family_id=207,
    abilities=[
        Attack(
            title="Ninja Fang",
            game_text="If, before Gliscor does damage, the Defending Pok\u00e9mon has no damage counters on it and is then damaged by this attack (after applying Weakness and Resistance), the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Poison Jab",
            game_text="The Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=condition_attack(SpecialConditions.POISONED),
        ),
    ],
)