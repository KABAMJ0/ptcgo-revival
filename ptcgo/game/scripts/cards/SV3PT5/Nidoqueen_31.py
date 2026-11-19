from ptcgo.game.card_effects.passives_common import protect_next_turn, attacker_is_basic, attacker_is_evolution
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bb7a5573-f971-5d2a-8b04-9436d20b661f",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nidoqueen.Name",
    display_name="Nidoqueen",
    searchable_by=["Nidoqueen", "Stage 2", "Nidoqueen"],
    subtypes=["Stage 2"],
    collector_number=31,
    set_code="SV3PT5",
    rarity=Rarities.Uncommon,
    hp=170,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nidorina.Name",
    family_id=29,
    abilities=[
        Attack(
            title="Queen Press",
            game_text="During your opponent's next turn, prevent all damage done to this Pok\u00e9mon by attacks from Basic Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=protect_next_turn(prevent=True, attacker_pred=attacker_is_basic()),
        ),
        Attack(
            title="Lunge Out",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
        ),
    ],
)