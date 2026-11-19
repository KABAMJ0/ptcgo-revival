from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8902a1f2-2831-5e5d-abc8-10243aa5feae",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkSlowking.Name",
    display_name="Dark Slowking",
    searchable_by=["Dark Slowking", "Stage 1", "DarkSlowking"],
    subtypes=["Stage 1"],
    collector_number=9,
    set_code="EX7",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.PSYCHIC, PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    family_id=79,
    abilities=[
        Ability(
            title="Cunning",
            game_text="Once during your turn (before your attack), you may look at the top card of your opponent's deck. Then, you may shuffle his or her deck. This power can't be used if Dark Slowking is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Litter",
            game_text="You may discard a combination of up to 2 Pok\u00e9mon Tool cards and Rocket's Secret Machine cards from your hand. If you do, this attack does 20 damage plus 30 more damage for each card you discarded.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)