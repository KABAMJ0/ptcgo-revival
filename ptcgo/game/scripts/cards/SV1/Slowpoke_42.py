from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.card_effects.support_common import heal_attack

card = PokemonCardDef(
    guid="8d78d4d3-29f6-544d-8845-ebfd30150858",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    display_name="Slowpoke",
    searchable_by=["Slowpoke", "Basic", "Slowpoke"],
    subtypes=["Basic"],
    collector_number=42,
    set_code="SV1",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=79,
    abilities=[
        Attack(
            title="Rest",
            game_text="This Pok\u00e9mon is now Asleep. Heal 30 damage from it.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=condition_attack(self_conditions=(SpecialConditions.ASLEEP,),
                            also=heal_attack(30, target="self")),
        ),
        Attack(
            title="Headbutt",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)