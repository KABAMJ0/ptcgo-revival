from ptcgo.game.card_effects.support_common import heal_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1944ba41-d34b-59d4-a0a6-4c9223b0805b",
    key="SV6PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Horsea.Name",
    display_name="Horsea",
    searchable_by=["Horsea", "Basic", "Horsea"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="SV6PT5",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=116,
    abilities=[
        Attack(
            title="Hold Still",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            effect=heal_attack(30),
        ),
        Attack(
            title="Razor Fin",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)