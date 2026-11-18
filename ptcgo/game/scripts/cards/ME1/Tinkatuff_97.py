from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9aaaebee-44d6-5d20-a162-29d013b4df76",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tinkatuff.Name",
    display_name="Tinkatuff",
    searchable_by=["Tinkatuff", "Stage 1", "Tinkatuff"],
    subtypes=["Stage 1"],
    collector_number=97,
    set_code="ME1",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tinkatink.Name",
    family_id=957,
    abilities=[
        Ability(
            title="Haphazard Hammer",
            game_text="Once during your turn, when you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon, you may use this Ability. Flip a coin. If heads, discard an Energy from your opponent's Active Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Light Punch",
            cost={PokemonTypes.METAL: 1},
            damage=30,
        ),
    ],
)