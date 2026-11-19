from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import protect_next_turn, attacker_is_basic

card = PokemonCardDef(
    guid="2ee619c9-eda0-56dd-b568-77942504c2b1",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Archaludon.Name",
    display_name="Archaludon",
    searchable_by=["Archaludon", "Stage 1", "Archaludon"],
    subtypes=["Stage 1"],
    collector_number=75,
    set_code="ME2",
    rarity=Rarities.Uncommon,
    hp=180,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Duraludon.Name",
    family_id=884,
    abilities=[
        Attack(
            title="Coated Attack",
            game_text="During your opponent's next turn, prevent all damage done to this Pok\u00e9mon by attacks from Basic Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 3},
            damage=120,
            effect=protect_next_turn(prevent=True, attacker_pred=attacker_is_basic()),
        ),
    ],
)