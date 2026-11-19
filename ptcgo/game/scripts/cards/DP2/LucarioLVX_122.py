from ptcgo.game.card_effects.passives_common import shield_source_next_turn
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Triggers
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4e652077-5824-5b86-9a1b-4587a102bf57",
    key="DP2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LucarioLVX.Name",
    display_name="Lucario LV.X",
    searchable_by=["Lucario LV.X", "Level-Up", "LucarioLVX"],
    subtypes=["Level-Up"],
    collector_number=122,
    set_code="DP2",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lucario.Name",
    family_id=448,
    abilities=[
        Ability(
            title="Stance",
            game_text="Once during your turn (before your attack), when you put Lucario LV.X from your hand onto your Active Lucario, you may use this power. Prevent all effects of an attack, including damage, done to Lucario during your opponent's next turn. (If Lucario is no longer your Active Pok\u00e9mon, this effect ends.)",
            trigger=Triggers.ON_PLAY,
            effect=shield_source_next_turn(prevent=True, effects_too=True),
        ),
        Attack(
            title="Close Combat",
            game_text="During your opponent's next turn, any damage done to Lucario by attacks is increased by 30 (after applying Weakness and Resistance).",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=unimplemented,
        ),
    ],
)