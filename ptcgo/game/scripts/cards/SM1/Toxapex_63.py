from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2033e680-f6c1-5611-a8c0-f5443ce6be46",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Toxapex.Name",
    display_name="Toxapex",
    searchable_by=["Toxapex", "Stage 1", "Toxapex"],
    subtypes=["Stage 1"],
    collector_number=63,
    set_code="SM1",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Mareanie.Name",
    family_id=747,
    abilities=[
        Ability(
            title="Toxic Spikes",
            game_text="Whenever your opponent's Active Pok\u00e9mon retreats, their new Active Pok\u00e9mon is Poisoned.",
            effect=unimplemented,
        ),
        Attack(
            title="Venoshock",
            game_text="If your opponent's Active Pok\u00e9mon is Poisoned, this attack does 50 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)