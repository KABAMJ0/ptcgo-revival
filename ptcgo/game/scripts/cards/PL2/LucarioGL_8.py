from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import count_energy, damage_per

card = PokemonCardDef(
    guid="6bb88789-2356-55db-ae26-41d86120366d",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LucarioGL.Name",
    display_name="Lucario GL",
    searchable_by=["Lucario GL", "Basic", "SP", "LucarioGL"],
    subtypes=["Basic", "SP"],
    collector_number=8,
    set_code="PL2",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=448,
    abilities=[
        Ability(
            title="Boundary Aura",
            game_text="Apply Weakness for each Pok\u00e9mon (both yours and your opponent's) as \u00d72 instead.",
            effect=unimplemented,
        ),
        Attack(
            title="Combo Throw",
            game_text="Does 30 damage plus 10 more damage for each Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=damage_per(count_energy("defender"), 10, base=30),
        ),
    ],
)