from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f9e20389-3779-58cc-8bed-3bb7160af044",
    key="SWSH9TG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Houndoom.Name",
    display_name="Houndoom",
    searchable_by=["Houndoom", "Stage 1", "Single Strike", "Houndoom"],
    subtypes=["Stage 1", "Single Strike"],
    collector_number=10,
    set_code="SWSH9TG",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Houndour.Name",
    family_id=229,
    abilities=[
        Ability(
            title="Single Strike Roar",
            game_text="Once during your turn, you may search your deck for a Single Strike Energy card and attach it to 1 of your Single Strike Pok\u00e9mon. Then, shuffle your deck. If you attached Energy to a Pok\u00e9mon in this way, put 2 damage counters on that Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Darkness Fang",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)