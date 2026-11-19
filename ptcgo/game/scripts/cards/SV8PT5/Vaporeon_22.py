from ptcgo.game.card_effects.support_common import heal_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import heal_attack

card = PokemonCardDef(
    guid="5ffd73c2-d2c3-56ea-9549-c6a3d25a022f",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vaporeon.Name",
    display_name="Vaporeon",
    searchable_by=["Vaporeon", "Stage 1", "Vaporeon"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="SV8PT5",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Spiral Drain",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            effect=heal_attack(30),
        ),
        Attack(
            title="Fighting Whirlpool",
            game_text="If your opponent's Active Pok\u00e9mon is a Pok\u00e9mon ex or Pok\u00e9mon V, this attack does 90 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)