from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d9f64ade-ee99-52f3-ac67-6f87347b013e",
    key="ME55C",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GreninjaBREAK.Name",
    display_name="Greninja BREAK",
    searchable_by=["Greninja BREAK", "BREAK", "GreninjaBREAK"],
    subtypes=["BREAK"],
    collector_number=41,
    set_code="ME55C",
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Greninja.Name",
    family_id=658,
    abilities=[
        Ability(
            title="Giant Water Shuriken",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is your Active Pok\u00e9mon, you may discard a Water Energy card from your hand. If you do, put 6 damage counters on 1 of your opponents Pok\u00e9mon.",
            effect=unimplemented,
        ),
    ],
)