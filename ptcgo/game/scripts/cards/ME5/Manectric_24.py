from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack

card = PokemonCardDef(
    guid="ab082e87-93d5-539a-80d6-560f205e0524",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Manectric.Name",
    display_name="Manectric",
    searchable_by=["Manectric", "Stage 1", "Manectric"],
    subtypes=["Stage 1"],
    collector_number=24,
    set_code="ME5",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Electrike.Name",
    family_id=309,
    abilities=[
        Attack(
            title="Flashing Barrier",
            game_text="During your opponent's next turn, prevent all damage done to this Pok\u00e9mon by attacks from Evolution Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=50,
            effect=unimplemented,
        ),
        Attack(
            title="Sonic Edge",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=110,
            effect=ignore_modifier_attack(ignore_target_effects=True),
        ),
    ],
)