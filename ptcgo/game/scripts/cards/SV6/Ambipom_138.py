from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0d55cadc-c847-5090-be50-7e578251b133",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ambipom.Name",
    display_name="Ambipom",
    searchable_by=["Ambipom", "Stage 1", "Ambipom"],
    subtypes=["Stage 1"],
    collector_number=138,
    set_code="SV6",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Aipom.Name",
    family_id=190,
    abilities=[
        Ability(
            title="Wicked Tail",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may flip 2 coins. For each heads, choose a random card from your opponent's hand. Your opponent reveals those cards and shuffles them into their deck.",
            effect=unimplemented,
        ),
        Attack(
            title="Gentle Slap",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
        ),
    ],
)