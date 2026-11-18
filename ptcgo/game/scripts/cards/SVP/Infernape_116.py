from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b1599438-b9da-5f53-a002-fd93c6b5b06f",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Infernape.Name",
    display_name="Infernape",
    searchable_by=["Infernape", "Stage 2", "Infernape"],
    subtypes=["Stage 2"],
    collector_number=116,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Monferno.Name",
    family_id=392,
    abilities=[
        Ability(
            title="Pyro Dance",
            game_text="Once during your turn, you may attach a Basic Fire Energy card, a Basic Fighting Energy card, or 1 of each from your hand to your Pok\u00e9mon in any way you like.",
            effect=unimplemented,
        ),
        Attack(
            title="Scorching Fire",
            game_text="Discard an Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=unimplemented,
        ),
    ],
)