from ptcgo.game.card_effects.support_common import heal_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e17b4163-bd18-570d-92ea-48c5c265df89",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Smoliv.Name",
    display_name="Smoliv",
    searchable_by=["Smoliv", "Basic", "Smoliv"],
    subtypes=["Basic"],
    collector_number=19,
    set_code="SV3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=928,
    abilities=[
        Attack(
            title="Absorb",
            game_text="Heal 10 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=heal_attack(10),
        ),
    ],
)