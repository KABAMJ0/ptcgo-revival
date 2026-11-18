from ptcgo.game.card_effects.support_common import heal_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ec928c3d-641a-5888-b50a-31a3ff875c1f",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WalkingWake.Name",
    display_name="Walking Wake",
    searchable_by=["Walking Wake", "Basic", "Ancient", "WalkingWake"],
    subtypes=["Basic", "Ancient"],
    collector_number=63,
    set_code="SV6",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=1009,
    abilities=[
        Attack(
            title="Aurora Gain",
            game_text="Heal 20 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            effect=heal_attack(20),
        ),
        Attack(
            title="Undulating Slice",
            game_text="Put up to 9 damage counters on this Pok\u00e9mon. This attack does 20 damage for each damage counter you placed in this way.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)