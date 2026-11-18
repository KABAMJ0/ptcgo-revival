from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="fc68e24d-f92e-52fb-a166-cf3c5e735ccd",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Linoone.Name",
    display_name="Linoone",
    searchable_by=["Linoone", "Stage 1", "Linoone"],
    subtypes=["Stage 1"],
    collector_number=82,
    set_code="ME2",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zigzagoon.Name",
    family_id=263,
    abilities=[
        Ability(
            title="Excited Dash",
            game_text="Once during your turn, if this Pok\u00e9mon is on your Bench, and if you have any Mega Evolution Pok\u00e9mon ex in play, you may use this Ability. Switch this Pok\u00e9mon with your Active Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Slash",
            cost={PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)