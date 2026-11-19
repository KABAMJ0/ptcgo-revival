from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import heal_attack

card = PokemonCardDef(
    guid="ab8ceab3-3658-5b55-878f-96d6c53e0a80",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tangrowth.Name",
    display_name="Tangrowth",
    searchable_by=["Tangrowth", "Stage 1", "Tangrowth"],
    subtypes=["Stage 1"],
    collector_number=7,
    set_code="ME1",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tangela.Name",
    family_id=114,
    abilities=[
        Attack(
            title="Absorb",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=heal_attack(30),
        ),
        Attack(
            title="Pumped-Up Whip",
            game_text="If this Pok\u00e9mon has at least 2 extra Energy attached (in addition to this attack's cost), this attack does 140 more damage.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2},
            damage=120,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)