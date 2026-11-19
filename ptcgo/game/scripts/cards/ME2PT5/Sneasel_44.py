from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import no_retreat_attack

card = PokemonCardDef(
    guid="0f2a2559-e7b9-52b3-9d96-abe554f0a06c",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sneasel.Name",
    display_name="Sneasel",
    searchable_by=["Sneasel", "Basic", "Sneasel"],
    subtypes=["Basic"],
    collector_number=44,
    set_code="ME2PT5",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=215,
    abilities=[
        Attack(
            title="Cut",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title="Beset",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.WATER: 2},
            damage=30,
            effect=no_retreat_attack(),
        ),
    ],
)