from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e80410c9-5f0a-5fb0-b1ae-035e8562445a",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Starmie.Name",
    display_name="Starmie",
    searchable_by=["Starmie", "Stage 1", "Starmie"],
    subtypes=["Stage 1"],
    collector_number=121,
    set_code="SV3PT5",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Staryu.Name",
    family_id=120,
    abilities=[
        Ability(
            title="Mysterious Comet",
            game_text="Once during your turn, you may put 2 damage counters on 1 of your opponent's Pok\u00e9mon. If you placed any damage counters in this way, discard this Pok\u00e9mon and all attached cards.",
            effect=unimplemented,
        ),
        Attack(
            title="Speed Attack",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)