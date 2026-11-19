from ptcgo.game.card_effects.attacks_common import no_weakness_next_turn
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import no_weakness_next_turn

card = PokemonCardDef(
    guid="618b663a-3cc5-5140-a5f0-687dc5616351",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Archaludonex.Name",
    display_name="Archaludon ex",
    searchable_by=["Archaludon ex", "Stage 1", "ex", "Archaludonex"],
    subtypes=["Stage 1", "ex"],
    collector_number=241,
    set_code="SV8",
    rarity=Rarities.Rare,
    hp=300,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Duraludon.Name",
    family_id=884,
    abilities=[
        Ability(
            title="Assemble Alloy",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may attach up to 2 Basic Metal Energy cards from your discard pile to your Metal Pok\u00e9mon in any way you like.",
            effect=unimplemented,
        ),
        Attack(
            title="Metal Defender",
            game_text="During your opponent's next turn, this Pok\u00e9mon has no Weakness.",
            cost={PokemonTypes.METAL: 3},
            damage=220,
            effect=no_weakness_next_turn(),
        ),
    ],
)